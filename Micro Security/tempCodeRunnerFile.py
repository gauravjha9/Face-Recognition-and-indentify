  cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)